var rowNumber = 1;
var prevNumberTI = 1;
var prevNumberTO = 1;


$(function() {
    $('.lined').on("click",function() {
        setLine(this);
    })
    $('.lined').keydown(function() {
        setLine(this);
    })
    $('.lined').keyup(function() {
        setLine(this);
    })
});

function setLine(t){
    rowNumber = t.value.substr(0, t.selectionStart).split("\n").length - 1;
    var t_node = t.parentNode.previousSibling.childNodes[0];
    if('textInput' == t.id){ 
        t_node.childNodes[prevNumberTI].className = "lineno"
        prevNumberTI = rowNumber;
    }
    else {
        t_node.childNodes[prevNumberTO].className = "lineno"
        prevNumberTO = rowNumber;
    }
    t_node.childNodes[rowNumber].className = "lineno lineselect"
}

$(".lined").linedtextarea({
    selectedLine: 0
 });