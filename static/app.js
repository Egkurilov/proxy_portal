$(document).ready(function() {
    var groupColumn = 3;
    var table = $('#index-table').DataTable({
        "columnDefs": [
            { "visible": false, "targets": groupColumn }
        ],
        "order": [[ groupColumn, 'asc' ]],
        "lengthMenu": [ [50, 75, 100, -1], [50, 75, 100, "All"] ],
        "columns": [
            null,
            null,
            null,
            null,
            {"width": "100px"},
            null,
            null,
            null,
            null,
            null,
        ],
        columnDefs: [{
		"render": function(data, type, row) {
			return(data == 'False' ? "DOWN" : "UP");
		},
		"targets": 8
	}],
        "displayLength": 25,
        "drawCallback": function ( settings ) {
            var api = this.api();
            var rows = api.rows( {page:'current'} ).nodes();
            var last=null;

            api.column(groupColumn, {page:'current'} ).data().each( function ( group, i ) {
                if ( last !== group ) {
                    $(rows).eq( i ).before(
                        '<tr class="group"><td colspan="10">'+group+'</td></tr>'
                    );

                    last = group;
                }
            } );
        }
    } );

    // Order by the grouping
    $('#index-table tbody').on( 'click', 'tr.group', function () {
        var currentOrder = table.order()[0];
        if ( currentOrder[0] === groupColumn && currentOrder[1] === 'asc' ) {
            table.order( [ groupColumn, 'desc' ] ).draw();
        }
        else {
            table.order( [ groupColumn, 'asc' ] ).draw();
        }
    } );
} );
