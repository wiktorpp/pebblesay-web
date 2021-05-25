term = new Terminal({
    cursorBlink: "block",
    scrollback: 1000,
    tabStopWidth: 8
});

term.open(document.getElementById('terminal-container'));