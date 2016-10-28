var webpack = require('webpack');
var path = require('path');

module.exports = {
	entry: [
		'./server/static/jsx/index.js'
	],
	devtool: 'inline-source-map',
	output: {
		path: path.join(__dirname, 'server/static/dist'),
		filename: 'bundle.js'
	},
	resolve: {
		extensions: ['', '.js']
	},
	module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react']
                },
                exclude: /node_modules/
                }
        ]
    },
	plugins: [
		new webpack.NoErrorsPlugin()
	]
};