const fs = require("fs"),
      NODE_ENV = "prod",
      path = require("path"),
      webpack = require("webpack");

module.exports = {
    entry: {
        main: ["babel-polyfill", "./frontend/app.js"]
    },
    output: {
        path: path.resolve("Project/static/js/"),
        publicPath: "/static/js/",
        filename: NODE_ENV === "prod"? "[name].[hash].js" : "[name].js"
    },
    externals: {
        "angular": "angular",
        "jquery": "jQuery",
        "uibootstrap": "'ui.bootstrap'",
        "moment": "moment",
    },
    resolve: {
        alias: {}
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                loaders: ["babel-loader"],
                include: /frontend/,
                exclude: /node_modules/
            },
            {
                test: /\.json$/,
                loader: "json-loader"
            }
        ]
    },
    watch: NODE_ENV != "prod",
    plugins: [
        new webpack.optimize.OccurrenceOrderPlugin(true),

        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: true,
                drop_console: NODE_ENV === "prod",
                unsafe: true
            },
            output: {
                comments: false
            },
            sourceMap: false
        }),

        function () {
            this.plugin("done", function (stats) {
                const replaceInJsFile = function (filePath, toReplace, replacement) {
                    const replacer = function (match) {
                        console.log('Replacing in %s: %s => %s', filePath, match, replacement);
                        return replacement;
                    };
                    const str = fs.readFileSync(filePath, "utf8");
                    const out = str.replace(/main\.?(.+)?\.js/gi, replacer);
                    fs.writeFileSync(filePath, out);
                };

                const {hash} = stats;

                if (NODE_ENV === "dev") {
                    replaceInJsFile(path.resolve("./templates/", "index.html"),
                      "main.js",
                      "main.js"
                    );
                } else {
                    replaceInJsFile(path.resolve("./templates/", "index.html"),
                      "main.js",
                      "main." + hash + ".js"
                    );
                }
            });
        }
    ],
    devtool: NODE_ENV === "prod"? false : "eval"
};