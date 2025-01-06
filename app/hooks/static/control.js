
const profilePic = document.querySelector('.profile-icn');
const profileDialog = document.querySelector('.profile-dialog');

console.log(profilePic);
console.log(profileDialog);

profilePic.addEventListener('click', () => {
  profileDialog.classList.toggle('show');
});

const boxcolor = document.getElementById('boxcolor');
const fontcolor = document.getElementById('fontcolor');
const textbg = document.getElementById('textbg');
const text = document.getElementById('text');

boxcolor.addEventListener('input', function () {
  textbg.style.background = boxcolor.value;
});

fontcolor.addEventListener('input', function () {
  text.style.color = fontcolor.value;
});
