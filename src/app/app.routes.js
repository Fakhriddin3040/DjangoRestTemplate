"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.routes = void 0;
var login_component_1 = require("./auth/login/login.component");
var register_component_1 = require("./auth/register/register.component");
var main_component_1 = require("./layout/main/main.component");
var product_list_component_1 = require("./features/products/components/product-list/product-list.component");
exports.routes = [
    { path: '', component: main_component_1.MainComponent, data: { breadcrumb: 'Home' } },
    { path: 'products', component: product_list_component_1.ProductListComponent, data: { breadcrumb: 'Products' } },
    { path: 'login', component: login_component_1.LoginComponent, data: { breadcrumb: 'Login' } },
    { path: 'register', component: register_component_1.RegisterComponent, data: { breadcrumb: 'Register' } },
];
