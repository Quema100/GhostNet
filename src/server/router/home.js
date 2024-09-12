module.exports = (app,path) =>{
    app.route('/Home')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'home.html'));
    })
    .post((req, res) => {
    
    })

    app.route('/setPort')
    .get((req, res) => {
    })
    .post((req, res) => {
        const { port } = req.body; 
        res.redirect(`/remotecontrol?port=${port}`); 
    })
}