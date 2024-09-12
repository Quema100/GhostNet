module.exports = (app,path) =>{
    app.route('/remotecontrol')
    .get((req, res) => {
        const port = req.query.port;
        if (port) res.sendFile(path.join(__dirname, '..', 'html', 'remotecontrol.html'));
        else return res.redirect('/Home')
    })
    .post((req, res) => {
    
    })
}