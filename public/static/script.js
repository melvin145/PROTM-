function ShowSidebar(toggle){
      const sidebar=document.getElementById("sidebar");
      sidebar.classList.toggle('show-sidebar');
}

const navbtn=document.querySelectorAll('.nav__btn');
const slide=document.querySelectorAll('.slider__item');
function ShowSlide(item){
      navbtn.forEach((nav)=>{
            nav.classList.remove('nav_active');
      })
      slide.forEach((s)=>{
            s.classList.remove('active');
      })
      navbtn[item].classList.add('nav_active');
      slide[item].classList.add('active');
}

navbtn.forEach((nav,i)=>{
      console.log(nav);
      nav.addEventListener('click',()=>{
            ShowSlide(i);
      })
})

function setActive(link){
      sidebarlinks.forEach((link)=>{
            link.classList.remove('active');
      })
      link.classList.add("active");
}
const sidebarlinks=document.querySelectorAll(".nav__link");
console.log(sidebarlinks);
sidebarlinks.forEach((link)=>{
      link.addEventListener('click',()=>{
            setActive(link)
      })
})
