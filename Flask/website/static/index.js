function deleteNote(noteId) {
    // to send a request in JS, we use fetch
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";//reloading window with get request specifically.
    });
}
// so this will take the noteid which we passed and send a POST request to end point which we had specified (/delete-note)
//and after it get response from deletenote end point, it will reload the window