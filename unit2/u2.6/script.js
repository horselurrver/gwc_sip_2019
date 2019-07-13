var allImages = ['images/landscape1.jpg', 'images/landscape2.jpg', 'images/landscape3.jpg']

// wrap index
function mod_floor(n) {
    let length = allImages.length;
    return ((n % length) + length) % length;
}

var index = 0;

function moveCarousel(direction) {
  $('#' + index).attr('class', 'far fa-circle center');
  if (direction === 'left') {
    index = index - 1;
  } else {
    index = index + 1;
  }
  index = mod_floor(index);
  $('#slideshow').attr('src', allImages[index]);
  $('#slideshow').fadeOut();
  $('#slideshow').fadeIn();
  $('#' + index).attr('class', 'fas fa-circle center');
}
function nextRight() {
  // alert('RIGHT');
  moveCarousel('right');
}

function nextLeft() {
  // alert('LEFT');
  moveCarousel('left');
}

rightArrow.onclick = nextRight;
leftArrow.onclick = nextLeft;
