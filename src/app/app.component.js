"use strict";
var __esDecorate = (this && this.__esDecorate) || function (ctor, descriptorIn, decorators, contextIn, initializers, extraInitializers) {
    function accept(f) { if (f !== void 0 && typeof f !== "function") throw new TypeError("Function expected"); return f; }
    var kind = contextIn.kind, key = kind === "getter" ? "get" : kind === "setter" ? "set" : "value";
    var target = !descriptorIn && ctor ? contextIn["static"] ? ctor : ctor.prototype : null;
    var descriptor = descriptorIn || (target ? Object.getOwnPropertyDescriptor(target, contextIn.name) : {});
    var _, done = false;
    for (var i = decorators.length - 1; i >= 0; i--) {
        var context = {};
        for (var p in contextIn) context[p] = p === "access" ? {} : contextIn[p];
        for (var p in contextIn.access) context.access[p] = contextIn.access[p];
        context.addInitializer = function (f) { if (done) throw new TypeError("Cannot add initializers after decoration has completed"); extraInitializers.push(accept(f || null)); };
        var result = (0, decorators[i])(kind === "accessor" ? { get: descriptor.get, set: descriptor.set } : descriptor[key], context);
        if (kind === "accessor") {
            if (result === void 0) continue;
            if (result === null || typeof result !== "object") throw new TypeError("Object expected");
            if (_ = accept(result.get)) descriptor.get = _;
            if (_ = accept(result.set)) descriptor.set = _;
            if (_ = accept(result.init)) initializers.unshift(_);
        }
        else if (_ = accept(result)) {
            if (kind === "field") initializers.unshift(_);
            else descriptor[key] = _;
        }
    }
    if (target) Object.defineProperty(target, contextIn.name, descriptor);
    done = true;
};
var __runInitializers = (this && this.__runInitializers) || function (thisArg, initializers, value) {
    var useValue = arguments.length > 2;
    for (var i = 0; i < initializers.length; i++) {
        value = useValue ? initializers[i].call(thisArg, value) : initializers[i].call(thisArg);
    }
    return useValue ? value : void 0;
};
var __setFunctionName = (this && this.__setFunctionName) || function (f, name, prefix) {
    if (typeof name === "symbol") name = name.description ? "[".concat(name.description, "]") : "";
    return Object.defineProperty(f, "name", { configurable: true, value: prefix ? "".concat(prefix, " ", name) : name });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AppComponent = void 0;
var core_1 = require("@angular/core");
var router_1 = require("@angular/router");
var header_component_1 = require("./layout/header/header.component");
var main_component_1 = require("./layout/main/main.component");
var footer_component_1 = require("./layout/footer/footer.component");
var login_component_1 = require("./auth/login/login.component");
var common_1 = require("@angular/common"); // Импортируйте CommonModule
var register_component_1 = require("./auth/register/register.component");
var breadcrumb_navigation_component_1 = require("./shared/components/breadcrumb-navigation/breadcrumb-navigation.component");
var container_component_1 = require("./shared/container/container.component");
var AppComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-root',
            standalone: true,
            imports: [
                router_1.RouterOutlet,
                header_component_1.HeaderComponent,
                main_component_1.MainComponent,
                footer_component_1.FooterComponent,
                login_component_1.LoginComponent,
                common_1.CommonModule,
                register_component_1.RegisterComponent,
                breadcrumb_navigation_component_1.BreadcrumbNavigationComponent,
                container_component_1.ContainerComponent
            ],
            templateUrl: './app.component.html',
            styleUrls: ['./app.component.scss'],
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var AppComponent = _classThis = /** @class */ (function () {
        function AppComponent_1() {
            this.title = 'marketplace-client';
            this.showMain = true;
        }
        // Функция для переключения на логин
        AppComponent_1.prototype.navigateToLogin = function () {
            this.showMain = false;
        };
        AppComponent_1.prototype.navigateToRegister = function () {
            this.showMain = false; // Переходим к компоненту Register
        };
        return AppComponent_1;
    }());
    __setFunctionName(_classThis, "AppComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        AppComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return AppComponent = _classThis;
}();
exports.AppComponent = AppComponent;
