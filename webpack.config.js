const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const ErrorLoggerPlugin = require('error-logger-webpack-plugin');



module.exports = {
    entry: './js_assets/index.js',  // path to our input file
    output: {
        filename: 'index-bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './static'),  // path to our Django static directory
    },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      // this will apply to both plain `.js` files
      // AND `<script>` blocks in `.vue` files
      {
        test: /\.js$/,
        loader: 'babel-loader'
      },
      // this will apply to both plain `.css` files
      // AND `<style>` blocks in `.vue` files
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader',
        ]
      }
    ]
  },
    plugins: [new VueLoaderPlugin(), new ErrorLoggerPlugin({verbose: false})]
};