


// ajax call to list, pulling back a list
// after pull a drop down is built

function list_return_drop_down() {
    $.getJSON('/list').done(function (data) {
        build_drop_down(data);
    });
};

// building list from json data
function build_drop_down(json_data) {
    var items = [];
    items.push('<select>');
    for (i = 0; i < json_data.result.length; i++) {
        items.push('<option value =' + i + '>' + json_data.result[i] + "</option>");
    }

    items.push("</select>");
    $("#result3").html(items.join(""));

};