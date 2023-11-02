/**
 * Created by beraaksoy on 2/6/17.
 */
$(document).ready(function () {

    // 1) Basic Table
    // Uncomment the next line and comment everything else for a basic table pagination and search
    // $('#maintable').DataTable();

    // 2) Hide columns 3 and 4
    // Use when you want to show a different view
    // $('#maintable').dataTable({
    //     "columnDefs": [
    //         {
    //             "targets": [2],
    //             "visible": false,
    //             "searchable": false
    //         },
    //         {
    //             "targets": [3],
    //             "visible": false
    //         }
    //     ]
    // });

    // 3) Add the following buttons:
    // - Show 10, 25, 50, 100, All rows
    // - Copy rows to clipboard
    // - Export to Excel
    // - Export to CSV
    // - Printable view
    // - Export to PDF
    // - Set column visibility
    var table = $('#maintable').DataTable({
        mark: true,
        dom: 'Bfrtip',
        lengthMenu: [
            [10, 25, 50, 100, -1],
            ['10行每页', '25行每页', '50行每页', '100行每页', '展示所有内容']
        ],
        buttons: [
            'pageLength',
            // {
            //     extend: 'copyHtml5',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
            // {
            //     extend: 'excelHtml5',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
            // {
            //     extend: 'csvHtml5',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
            // {
            //     extend: 'print',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
            // {
            //     extend: 'pdfHtml5',
            //     download: 'open',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
            'colvis'
        ],
        columDefs: [{
            targets: -1,
            visible: false
        }]
    });

    // 4) Search on Multiple Columns
    $('#maintable tfoot th').each(function () {
        var title = $('#maintable tfoot th').eq($(this).index()).text();
        $(this).html('<input type="text" placeholder="按照 ' + title + ' 查找" />');
    });

    table.columns().eq(0).each(function (colIdx) {
        $('input', table.column(colIdx).footer()).on('keyup change', function () {
            table
                .column(colIdx)
                .search(this.value)
                .draw();
        });
    });

});
