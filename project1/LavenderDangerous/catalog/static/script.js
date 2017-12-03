function searchURL(){
    window.location.href = "products?q="+document.getElementById("search_main").value;
    return false;
}