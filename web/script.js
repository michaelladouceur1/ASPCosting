function setVal(item) {
    items = $(item);
    table = item.split('.').join('')
    values = {}
    for (i=0; i<items.length; i++) {
        console.log($(items[i]).val())
        console.log($(items[i]).attr('name'))
        values[$(items[i]).attr('name')] = ($(items[i]).val())
    }
    eel.setValue(table, values);
};

function loadSelect(classSelect) {
	
}