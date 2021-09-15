var rowNumber = 1;
var prevNumberTI = 1;
var prevNumberTO = 1;


$(function() {
    $('.lined').on("click",function() {
        setLine(this);
    })
    $('.lined').keydown(function(e) {
        if (e.keyCode == 9){
            // get caret position/selection
            var val = this.value,
                start = this.selectionStart,
                end = this.selectionEnd;

            // set textarea value to: text before caret + tab + text after caret
            this.value = val.substring(0, start) + '\t' + val.substring(end);

            // put caret at right position again
            this.selectionStart = this.selectionEnd = start + 1;

            // prevent the focus lose
            return false;
        }
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