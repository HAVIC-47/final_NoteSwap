const container = document.getElementById("container");
const registerbtn = document.getElementById("register");
const loginbtn = document.getElementById("login");

registerbtn.addEventListener("click", () => {
  container.classList.add("active");
});

loginbtn.addEventListener("click", () => {
  container.classList.remove("active");
});



// script.js

document.addEventListener('DOMContentLoaded', () => {
  const menuBtn = document.getElementById('menu-btn');
  const navbar = document.querySelector('.header .navbar');

  menuBtn.addEventListener('click', () => {
      navbar.classList.toggle('active');
      menuBtn.classList.toggle('fa-times'); // Toggle icon if you are using Font Awesome
  });
});

