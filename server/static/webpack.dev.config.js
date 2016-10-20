var path = require('path');
var webpack = require('webpack');

module.exports = {
    devtool: 'inline-source-map',
    entry: [
        './jsx',
    ],
    output: {
        path: path.join(__dirname, 'dist'),
        filename: 'bundle.js'
    },
    resolve: {
        modulesDirectories: ['../../node_modules'],
        extensions: ['', '.js']
    },
    module: {
    loaders: [
         {
             test: /\.js$/,
             loader: ['babel', 'react-hot'],
             query: {
                 presets: ['react', 'es2015']
             }
         }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin()
    ]
};