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
exports.Section9HomeGardenKitchenComponent = void 0;
var core_1 = require("@angular/core");
var common_1 = require("@angular/common");
var container_component_1 = require("../../../shared/container/container.component");
var button_shop_now_component_1 = require("../../../shared/components/buttons/button-shop-now/button-shop-now.component");
var Section9HomeGardenKitchenComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-section9-home-garden-kitchen',
            standalone: true,
            imports: [container_component_1.ContainerComponent, button_shop_now_component_1.ButtonShopNowComponent],
            templateUrl: './section9-home-garden-kitchen.component.html',
            styleUrl: './section9-home-garden-kitchen.component.scss'
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var Section9HomeGardenKitchenComponent = _classThis = /** @class */ (function () {
        function Section9HomeGardenKitchenComponent_1(renderer, platformId) {
            this.renderer = renderer;
            this.platformId = platformId;
            this.scriptLoaded = false;
        }
        Section9HomeGardenKitchenComponent_1.prototype.ngOnInit = function () {
            var _this = this;
            if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                // Загружаем скрипт и стили для Swiper, если они еще не загружены
                var script = this.renderer.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.js';
                script.onload = function () {
                    _this.scriptLoaded = true;
                    _this.initializeSwiper();
                };
                script.onerror = function (error) {
                    console.error('Ошибка загрузки скрипта Swiper:', error);
                };
                this.renderer.appendChild(document.body, script);
                var link = this.renderer.createElement('link');
                link.rel = 'stylesheet';
                link.href = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.css';
                this.renderer.appendChild(document.head, link);
            }
        };
        Section9HomeGardenKitchenComponent_1.prototype.ngAfterViewInit = function () {
            if (this.scriptLoaded) {
                this.initializeSwiper();
            }
            if ((0, common_1.isPlatformBrowser)(this.platformId)) {
                var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
                tooltipTriggerList.map(function (tooltipTriggerEl) {
                    return new window.bootstrap.Tooltip(tooltipTriggerEl);
                });
            }
        };
        Section9HomeGardenKitchenComponent_1.prototype.initializeSwiper = function () {
            if (window['Swiper']) {
                var Swiper = window['Swiper'];
                var swiper = new Swiper(".section6Swiper", {
                    slidesPerView: 3,
                    grid: {
                        rows: 2,
                    },
                    pagination: {
                        el: ".swiper-pagination",
                        clickable: true,
                    },
                });
            }
            else {
                console.error('Swiper не найден.');
            }
        };
        return Section9HomeGardenKitchenComponent_1;
    }());
    __setFunctionName(_classThis, "Section9HomeGardenKitchenComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        Section9HomeGardenKitchenComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return Section9HomeGardenKitchenComponent = _classThis;
}();
exports.Section9HomeGardenKitchenComponent = Section9HomeGardenKitchenComponent;
