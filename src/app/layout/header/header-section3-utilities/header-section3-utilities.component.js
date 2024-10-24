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
exports.HeaderSection3UtilitiesComponent = void 0;
var core_1 = require("@angular/core");
var info_user_component_1 = require("../../../user/info-user/info-user.component");
var login_component_1 = require("../../../auth/login/login.component");
var router_1 = require("@angular/router");
var common_1 = require("@angular/common");
var container_component_1 = require("../../../shared/container/container.component");
var HeaderSection3UtilitiesComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-header-section3-utilities',
            standalone: true,
            imports: [
                common_1.CommonModule,
                info_user_component_1.InfoUserComponent,
                login_component_1.LoginComponent,
                container_component_1.ContainerComponent,
                router_1.RouterModule
            ],
            templateUrl: './header-section3-utilities.component.html',
            styleUrls: ['./header-section3-utilities.component.scss']
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var _loginModal_decorators;
    var _loginModal_initializers = [];
    var _loginModal_extraInitializers = [];
    var _loginClick_decorators;
    var _loginClick_initializers = [];
    var _loginClick_extraInitializers = [];
    var HeaderSection3UtilitiesComponent = _classThis = /** @class */ (function () {
        function HeaderSection3UtilitiesComponent_1(modalService, router, authService) {
            this.modalService = modalService;
            this.router = router;
            this.authService = authService;
            this.selected = 'option2';
            this.loginModal = __runInitializers(this, _loginModal_initializers, void 0);
            this.loginClick = (__runInitializers(this, _loginModal_extraInitializers), __runInitializers(this, _loginClick_initializers, new core_1.EventEmitter()));
            this.isUserLoggedIn = (__runInitializers(this, _loginClick_extraInitializers), false);
        }
        HeaderSection3UtilitiesComponent_1.prototype.navigateToLogin = function () {
            console.log('navigateToLogin method called');
            var loginComponent = document.getElementById('content');
            if (loginComponent) {
                this.modalService.open(loginComponent, { centered: true });
            }
        };
        HeaderSection3UtilitiesComponent_1.prototype.ngOnInit = function () {
            var _this = this;
            // Подписываемся на изменения состояния авторизации
            this.authService.isLoggedIn$.subscribe(function (loggedIn) {
                _this.isUserLoggedIn = loggedIn;
            });
        };
        HeaderSection3UtilitiesComponent_1.prototype.navigateToRegister = function () {
            console.log('Register link clicked');
            this.router.navigate(['/register'])
                .then(function (success) {
                if (success) {
                    console.log('Navigation to register successful');
                }
                else {
                    console.error('Navigation to register failed');
                }
            })
                .catch(function (err) {
                console.error('Navigation error:', err);
            });
        };
        return HeaderSection3UtilitiesComponent_1;
    }());
    __setFunctionName(_classThis, "HeaderSection3UtilitiesComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        _loginModal_decorators = [(0, core_1.ViewChild)('loginModal')];
        _loginClick_decorators = [(0, core_1.Output)()];
        __esDecorate(null, null, _loginModal_decorators, { kind: "field", name: "loginModal", static: false, private: false, access: { has: function (obj) { return "loginModal" in obj; }, get: function (obj) { return obj.loginModal; }, set: function (obj, value) { obj.loginModal = value; } }, metadata: _metadata }, _loginModal_initializers, _loginModal_extraInitializers);
        __esDecorate(null, null, _loginClick_decorators, { kind: "field", name: "loginClick", static: false, private: false, access: { has: function (obj) { return "loginClick" in obj; }, get: function (obj) { return obj.loginClick; }, set: function (obj, value) { obj.loginClick = value; } }, metadata: _metadata }, _loginClick_initializers, _loginClick_extraInitializers);
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        HeaderSection3UtilitiesComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return HeaderSection3UtilitiesComponent = _classThis;
}();
exports.HeaderSection3UtilitiesComponent = HeaderSection3UtilitiesComponent;
