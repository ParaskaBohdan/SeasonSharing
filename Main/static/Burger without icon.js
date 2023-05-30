window.addEventListener('DOMContentLoaded', () => {
      
   const burgerMenu = document.querySelector('.burger-menu');
   const mobileMenu = document.querySelector('.mobile-menu');

   burgerMenu.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      if (mobileMenu.classList.contains('open')) {
         mobileMenu.style.display = 'block';
      } else {
         mobileMenu.style.display = 'none';
      }
   });
});