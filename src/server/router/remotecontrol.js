let remotecontrol = (app,path) =>{
    app.route('/control')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'remotecontrol.html'));
    })
    .post((req, res) => {
    
    })
}

module.exports= remotecontrol