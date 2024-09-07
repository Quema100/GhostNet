let home = (app,path) =>{
    app.route('/Home')
    .get((req, res) => {
        res.sendFile(path.join(__dirname, '..', 'html', 'home.html'));
    })
    .post((req, res) => {
    
    })
}

module.exports= home