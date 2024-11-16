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
exports.LoginComponent = void 0;
var core_1 = require("@angular/core");
var common_1 = require("@angular/common");
var LoginComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-login',
            standalone: true,
            templateUrl: './login.component.html',
            styleUrls: ['./login.component.scss'],
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var _content_decorators;
    var _content_initializers = [];
    var _content_extraInitializers = [];
    var LoginComponent = _classThis = /** @class */ (function () {
        function LoginComponent_1(modalService, authService) {
            this.modalService = modalService;
            this.authService = authService;
            this.platformId = (0, core_1.inject)(core_1.PLATFORM_ID);
            this.content = __runInitializers(this, _content_initializers, void 0);
            __runInitializers(this, _content_extraInitializers);
            this.modalService = modalService;
            this.authService = authService;
        }
        LoginComponent_1.prototype.ngAfterViewInit = function () {
            // Проверка, что шаблон инициализирован
            if (this.content) {
                console.log('Template initialized:', this.content);
            }
            else {
                console.log('Template not found');
            }
        };
        LoginComponent_1.prototype.navigateToLogin = function () {
            var _this = this;
            console.log('navigateToLogin method called');
            if (this.content) {
                var modalRef = this.modalService.open(this.content, { centered: true });
                modalRef.result.then(function () { }, function () {
                    console.log('Modal closed');
                });
                // Рендерим кнопку Google после полной инициализации модального окна
                modalRef.shown.subscribe(function () {
                    setTimeout(function () { return _this.renderGoogleButton(); }, 0); // Ожидаем рендер модального окна
                });
            }
            else {
                console.log('Template not found');
            }
        };
        LoginComponent_1.prototype.renderGoogleButton = function () {
            var _this = this;
            if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                this.loadGoogleScript().then(function () {
                    google.accounts.id.initialize({
                        client_id: '409809896736-fckja2ujg9itegt7r06k2itrt409472a.apps.googleusercontent.com',
                        callback: function (response) {
                            _this.handlelogin(response); // Обработка логина
                            return false;
                        },
                    });
                    google.accounts.id.renderButton(document.getElementById('googleSignInButtonModal'), // Убедитесь, что ID совпадает с элементом в шаблоне
                    { theme: 'outline', size: 'large' });
                });
            }
        };
        LoginComponent_1.prototype.ngOnInit = function () {
            if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                this.loadGoogleScript();
            }
        };
        LoginComponent_1.prototype.loadGoogleScript = function () {
            return new Promise(function (resolve, reject) {
                if (typeof google !== 'undefined') {
                    resolve();
                }
                else {
                    var script = document.createElement('script');
                    script.src = 'https://accounts.google.com/gsi/client';
                    script.async = true;
                    script.defer = true;
                    script.onload = function () { return resolve(); };
                    script.onerror = function (error) {
                        console.error('Error loading Google script:', error);
                        reject(error);
                    };
                    document.body.appendChild(script);
                }
            });
        };
        LoginComponent_1.prototype.decoderToken = function (token) {
            return JSON.parse(atob(token.split('.')[1]));
        };
        LoginComponent_1.prototype.handlelogin = function (response) {
            if (response) {
                try {
                    var payload = this.decoderToken(response.credential);
                    if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                        // Используем AuthService для обновления состояния
                        this.authService.setLoggedInUser({
                            name: payload.name,
                            email: payload.email,
                            picture: payload.picture,
                        }, response.credential);
                    }
                }
                catch (error) {
                    console.error('Error handling login response:', error);
                }
            }
        };
        return LoginComponent_1;
    }());
    __setFunctionName(_classThis, "LoginComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        _content_decorators = [(0, core_1.ViewChild)('content')];
        __esDecorate(null, null, _content_decorators, { kind: "field", name: "content", static: false, private: false, access: { has: function (obj) { return "content" in obj; }, get: function (obj) { return obj.content; }, set: function (obj, value) { obj.content = value; } }, metadata: _metadata }, _content_initializers, _content_extraInitializers);
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        LoginComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return LoginComponent = _classThis;
}();
exports.LoginComponent = LoginComponent;
