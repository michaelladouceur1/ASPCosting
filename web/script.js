function setVal(item) {
    items = $(item);
    table = item.split('.').join('');
    values = {};
    for (i=0; i<items.length; i++) {
        values[$(items[i]).attr('name')] = ($(items[i]).val())
    };
    eel.setValue(table, values);
    eel.loadTable(table, Object.keys(values));
};

eel.expose(loadTable);
function loadTable(items, table) {
    selector = '#' + table + 'Table';
	$(selector).empty()
	Object.keys(items).forEach((key) => {
        values = ''
        Object.values(items[key]).forEach((item) => {
            values += '<td>' + item + '</td>';
        });
        $(selector).append(
        '<tr class="' + table +'-' + key +'">' +
            values +
            '<td>' +
                '<a href="#"><i class="material-icons">settings</i></a>' +
                '<button type="button" class="close" aria-label="Close">' +
                    '<span aria-hidden="true">&times;</span>' +
                '</button>' +
            '</td>' +
        '</tr>'
        );
	});
};

eel.expose(loadSelect);
function loadSelect(items, table) {
    console.log('JS LOADSELECT');
    selector = '#' + table + 'Select';
    $(selector).empty()
    Object.keys(items).forEach((key) => {
        values = ''
        Object.values(items[key]).forEach((item) => {
            values += '<option class="' + table + '-' + key + '" value="' + item + '">' + item +'</option>';
        });
        $(selector).append(values);
	});
}

function deleteTableItem(target) {
    rowClass = $(target).closest('tr').attr('class');
    collection = rowClass.split('-')[0];
    id = rowClass.split('-')[1];
    eel.removeValue(collection, id=id);
	$(target).closest('tr').remove();
}

eel.expose(init);
function init() {
	$(document).ready(function() {
		$(".close").click(function(event) {
			deleteTableItem(event.target);
		});
	});
};
