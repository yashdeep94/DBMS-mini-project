let total = 0;
let all_checkbox = document.querySelectorAll(".form-check-input");

Array.from(all_checkbox).forEach(function(checkbox){
    checkbox.addEventListener("click", check);
})

let rates = {
    "starPlusHD" : 18, 
    "zeeTvHD" : 15,
    "colorsHD" : 20,
    "&tvHD" : 19,
    "zeeMarathiHD" : 17,
    "starPravahHD" : 14,
    "zeeTalkiesHD" : 15,
    "colorsMarathiHD" : 17,
    "starGoldHD" : 19,
    "setMaxHD" : 20,
    "zeeCinemaHD" : 15,
    "&PicturesHD" : 19,
    "starMoviesHD" : 21,
    "sonyPixHD" : 22,
    "moviesNowHD" : 25,
    "&FlixHD" : 20
}

function check(e){
    let element = document.getElementById(e.target.id);
    let total_block = document.getElementById("total_block");
    let total_outer = document.getElementById("total_outer");
    let total_val = document.getElementById("total_value");
    if (element.checked == true){
        total_outer.style.display = "block";
        total += rates[element.id];
        total_block.innerHTML = `${total}`;
        total_val.value = `${total}`;
    }
    else {
        total -= rates[element.id];
        total_block.innerHTML = `${total}`;
        total_val.value = `${total}`;
    }
}