window.addEventListener('DOMContentLoaded', () => {
   const userBlock = document.querySelector('.user-block');
   const dropdownList = document.querySelector('.dropdownlist');

   userBlock.addEventListener('click', (event) => {
      event.stopPropagation();
      dropdownList.style.display = dropdownList.style.display === 'block' ? 'none' : 'block';
      mobileMenu.style.display = 'none';
      if (mobileMenu.classList.contains('open')) {
         mobileMenu.classList.toggle('open');
      }
   });

   document.addEventListener('click', (event) => {
      const target = event.target;
      if (!userBlock.contains(target) && !dropdownList.contains(target)) {
         dropdownList.style.display = 'none';
      }
   });

   const burgerMenu = document.querySelector('.burger-menu');
   const mobileMenu = document.querySelector('.mobile-menu');

   burgerMenu.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      if (mobileMenu.classList.contains('open')) {
         mobileMenu.style.display = 'block';
         dropdownList.style.display = 'none';
      } else {
         mobileMenu.style.display = 'none';
      }
   });
});