

$(function(){

	window.audio = new Audio();
const volumeSlider = document.getElementById('volume-slider');
const outputContainer = document.getElementById('volume-output');
	const durationContainer = document.getElementById('duration');
	const playIconContainer = document.getElementById('play-icon');
	const seekSlider = document.getElementById('seek-slider');
const currentTimeContainer = document.getElementById('current-time');
	var playState="pause";



window.audio.addEventListener('loadedmetadata', () => {
  displayDuration(window.audio.duration);
});

	const calculateTime = (secs) => {
  const minutes = Math.floor(secs / 60);
  const seconds = Math.floor(secs % 60);
  const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
  return `${minutes}:${returnedSeconds}`;
}
const displayDuration = () => {
  durationContainer.textContent = calculateTime(window.audio.duration);
}

if (window.audio.readyState > 0) {
  displayDuration();
} else {
  window.audio.addEventListener('loadedmetadata', () => {
    displayDuration();
  });
}


const setSliderMax = () => {
  seekSlider.max = Math.floor(window.audio.duration);
}

if (window.audio.readyState > 0) {
  displayDuration();
  setSliderMax();
} else {
  window.audio.addEventListener('loadedmetadata', () => {
    displayDuration();
    setSliderMax();
  });
}





playIconContainer.addEventListener('click', () => {
  if(playState === 'play') {
    window.audio.play();
    playState = 'pause';

    playIconContainer.innerHTML=(playIconContainer.dataset.pause);
  } else {
    window.audio.pause();
    playState = 'play';
    playIconContainer.innerHTML =(playIconContainer.dataset.play);

  }
});
window.audio.addEventListener('timeupdate', () => {
  seekSlider.value = Math.floor(window.audio.currentTime);
  currentTimeContainer.textContent = calculateTime(seekSlider.value);
});


seekSlider.addEventListener('input', () => {

  window.audio.currentTime = seekSlider.value;


  if(!window.audio.paused) {
	  whilePlaying();
  }
});

seekSlider.addEventListener('change', () => {
  window.audio.currentTime = seekSlider.value;



  if(!window.audio.paused) {
	  whilePlaying();
  }
});
const whilePlaying = () => {
  seekSlider.value = Math.floor(window.audio.currentTime);
  currentTimeContainer.textContent = calculateTime(seekSlider.value);
}


volumeSlider.addEventListener('input', (e) => {
  const value = e.target.value;

  outputContainer.textContent = value;
  window.audio.volume = value / 100;
});
const muteIconContainer = document.getElementById('mute-icon');

muteIconContainer.addEventListener('click', () => {
  if(muteState === 'unmute') {
    muteAnimation.playSegments([0, 15], true);
    window.audio.muted = true;
    muteState = 'mute';
  } else {
    muteAnimation.playSegments([15, 25], true);
    window.audio.muted = false;
    muteState = 'unmute';
  }
});
$("[name='image']").on('change', function () {
  var file = this.files[0];

  if (file.size > 1024) {
    alert('max upload size is 1k');
  }

  // Also see .name, .type
});
$('#recordingform').on('submit', function () {
  $.ajax({
    // Your server script to process the upload
    url: '/recording',
    type: 'POST',

    // Form data
    data: new FormData($('#recordingform')[0]),

    // Tell jQuery not to process data or worry about content-type
    // You *must* include these options!
    cache: false,
    contentType: false,
    processData: false,

    // Custom XMLHttpRequest
    success: function (data) {
	    window.location="/allmymusic";
    },
    xhr: function () {
      var myXhr = $.ajaxSettings.xhr();
      if (myXhr.upload) {
        // For handling the progress of the upload
        myXhr.upload.addEventListener('progress', function (e) {
          if (e.lengthComputable) {
            $('progress').attr({
              value: e.loaded,
              max: e.total,
            });
          }
        }, false);
      }
      return myXhr;
    }
  });
	return false;
});
});
