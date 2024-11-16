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
exports.ProductListComponent = void 0;
var core_1 = require("@angular/core");
var breadcrumb_navigation_component_1 = require("../../../../shared/components/breadcrumb-navigation/breadcrumb-navigation.component");
var container_component_1 = require("../../../../shared/container/container.component");
var router_1 = require("@angular/router");
var product_section1_slide_component_1 = require("./product-section1-slide/product-section1-slide.component");
var product_section2_our_partners_component_1 = require("./product-section2-our-partners/product-section2-our-partners.component");
var product_section3_category_electronics_component_1 = require("./product-section3-category-electronics/product-section3-category-electronics.component");
var product_section4_filter_component_1 = require("./product-section4-filter/product-section4-filter.component");
var ProductListComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-product-list',
            standalone: true,
            imports: [breadcrumb_navigation_component_1.BreadcrumbNavigationComponent, container_component_1.ContainerComponent, router_1.RouterOutlet, product_section1_slide_component_1.ProductSection1SlideComponent, product_section2_our_partners_component_1.ProductSection2OurPartnersComponent, product_section3_category_electronics_component_1.ProductSection3CategoryElectronicsComponent, product_section4_filter_component_1.ProductSection4FilterComponent],
            templateUrl: './product-list.component.html',
            styleUrl: './product-list.component.scss'
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var ProductListComponent = _classThis = /** @class */ (function () {
        function ProductListComponent_1() {
        }
        return ProductListComponent_1;
    }());
    __setFunctionName(_classThis, "ProductListComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        ProductListComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return ProductListComponent = _classThis;
}();
exports.ProductListComponent = ProductListComponent;
