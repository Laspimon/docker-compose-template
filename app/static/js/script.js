function make_request() {
    var XHR = new XMLHttpRequest();
    var FD  = new FormData();
    FD.append('name', document.getElementById('name').value);

    XHR.addEventListener('load', function(event) {
        let json_data = JSON.parse(event.currentTarget.response);
        document.getElementById('response').value = json_data['data'];
    });
    XHR.addEventListener('error', function(event) {
        document.getElementById('response').value = 'Error.';
    });

    XHR.open('POST', '/greeter');
    XHR.send(FD);
}
