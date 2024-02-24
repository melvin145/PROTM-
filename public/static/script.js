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
      localStorage.setItem('active',link.id)
}
const sidebarlinks=document.querySelectorAll(".nav__link");
function CheckActive(){   
      if(localStorage.getItem('active')!=' '){
            document.getElementById(localStorage.getItem('active')).classList.add('active')
      }
      sidebarlinks.forEach((link)=>{
      link.addEventListener('click',()=>{
      setActive(link);
      })
      })
}
CheckActive()

function showFilter(){
      const button=document.querySelectorAll('.btn')
      const dropdown=document.querySelectorAll('.drop')
      button.forEach((btn,key)=>{
            btn.addEventListener('click',()=>{
                  dropdown[key].classList.toggle('hidden')
                  dropdown[key].classList.toggle('dropdown')
            })
      })
}
showFilter()


function filterByCategory(){
      let checkboxes=document.querySelectorAll('input[type="checkbox"]')
      checkboxes.forEach((check)=>{
            if(check.checked==true && check.value!='all'){
                  const url=new URL(window.location.href)
                  const searchparams=url.searchParams;
                  searchparams.set('category',check.value)
                  console.log(searchparams)
                  url.search=searchparams.toString()
                  console.log(url.search)
                  const new_url=url.toString()
                  window.location.href=new_url
            }
            else if(check.checked==true && check.value=='all'){
                  window.location.href='http://127.0.0.1:8000/listproducts/'
            }
      })
}


function SortProducts(){
      let checkboxes=document.querySelectorAll('.sort_item')
      checkboxes.forEach((check)=>{
            check.addEventListener('click',()=>{
                  url=new URL(window.location.href)
                  const searchparams=url.searchParams;
                  console.log(check.value)
                  searchparams.set('ordering',check.value)
                  url.search=searchparams.toString()
                  const new_url=url.toString()
                  window.location.href=new_url
            })
      })
}
SortProducts()

function SearchProduct(){
      const search=document.getElementById('search')
      const url=new URL('http://127.0.0.1:8000/listproducts/')
      const searchparam=url.searchParams;
      searchparam.set("search",search.value)
      url.search=searchparam.toString();
      const new_url=url.toString()
      window.location.href=new_url;
}