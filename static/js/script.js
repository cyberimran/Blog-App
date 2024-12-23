let menulist = document.getElementById("menu-list")
menulist.style.maxHeight = "0px";

function toggleMenu(){
    if (menulist.style.maxHeight == "0px"){
        menulist.style.maxHeight = "310px";
    }
    else{
        menulist.style.maxHeight = "0px";
    }
}

function searchMenu(){
    var search = document.getElementById("search-container");
    if (search.style.display == "flex"){
        search.style.display = "none";
    }
    else{
        search.style.display = "flex";
        if (menulist.style.maxHeight=="310px"){
            menulist.style.maxHeight = "0px";
        }
    }
}