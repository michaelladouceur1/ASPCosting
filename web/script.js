function setVal(item) {
    items = $(item);
    table = item.split('.').join('');
    values = {};
    for (i=0; i<items.length; i++) {
        values[$(items[i]).attr('name')] = ($(items[i]).val())
    };
    eel.setValue(table, values);
    eel.loadTable('materialType', ['name'])
};

eel.expose(loadTable);
function loadTable(items, selector) {
	$(selector).empty()
	index = 0;
	items.forEach((item) => {
		$(selector).append(
    	'<tr>' +
    		'<td>' + item + '</td>' +
    		'<td>' +
    			'<a href="#"><i class="material-icons">settings</i></a>' +
    			'<button type="button" class="delete" aria-label="Close">' +
					'<span aria-hidden="true">&times;</span>' +
				'</button>' +
    		'</td>' +
    	'</tr>'
    	);
	});
};

function deleteTableItem(target) {
	$(target).closest('tr').remove()
}

eel.expose(init);
function init() {
	$(document).ready(function() {
		$(".delete").click(function(event) {
			deleteTableItem(event.target);
		});
	});
};
