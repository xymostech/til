var timeElems = document.getElementsByClassName("time");

for (var i = 0; i < timeElems.length; i++) {
    var timeElem = timeElems[i];

    var time = moment.utc(timeElem.innerText).local();

    timeElem.innerText = time.format("h:mm");
}
