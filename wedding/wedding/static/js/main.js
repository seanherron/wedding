function getTimeRemaining(endtime) {
  var t = Date.parse(endtime) - Date.parse(new Date());
  var seconds = Math.floor((t / 1000) % 60);
  var minutes = Math.floor((t / 1000 / 60) % 60);
  var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
  var days = Math.floor(t / (1000 * 60 * 60 * 24));
  return {
    'total': t,
    'days': days,
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds
  };
}

function initializeClock(id, endtime) {
  var clock = document.getElementById(id);
  var daysSpan = clock.querySelector('.days');
  var hoursSpan = clock.querySelector('.hours');
  var minutesSpan = clock.querySelector('.minutes');
  var secondsSpan = clock.querySelector('.seconds');

  function updateClock() {
    var t = getTimeRemaining(endtime);

    daysSpan.innerHTML = t.days;
    hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
    minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}

var deadline = 'April 22 2017 17:30:00 GMT-0700'
initializeClock('countdown-clock', deadline);

L.mapbox.accessToken = 'pk.eyJ1Ijoic2VhbmhlcnJvbjEiLCJhIjoiY2l4engweXR2MDA3ajMzbXNzbWl4b3ZseiJ9.FzAcenDq4-hIqzPnHDmNig';
var map = L.mapbox.map('map', 'mapbox.streets', {
    attributionControl: {
      compact: true
    },
    scrollWheelZoom: false
})
    .setView([34.07, -118.6931326], 11);

var marker = L.marker([34.0781926, -118.6931326], {
      icon: L.mapbox.marker.icon({
        'marker-color': '#E37222',
        'marker-size': 'large'
      })
    })
    .addTo(map);

var saddlepeakpopup = L.popup({
    closeOnClick: false,
    closeButton: false
  }).setContent('<center><strong>Saddle Peak Lodge</strong><br>419 Cold Canyon Road<br>Malibu Canyon, California 91302</center>');

marker.bindPopup(saddlepeakpopup).openPopup();
