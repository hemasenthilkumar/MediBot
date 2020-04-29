
function reply_click(obj)
{
var id = obj.id;
var url ="http://127.0.0.1:5000/delete/" + id;
window.location = url;
}
