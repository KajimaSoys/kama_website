import {createRouter, createWebHistory} from 'vue-router'
import CatalogView from "../views/CatalogView.vue";
import DeliveryView from "../views/DeliveryView.vue";
import MainView from "../views/MainView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import PolicyView from "../views/PolicyView.vue";
import ProductView from "../views/ProductView.vue";
import ReviewsView from "../views/ReviewsView.vue";
import TermsView from "../views/TermsView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/catalog',
            name: 'catalog',
            component: CatalogView
        },
        {
            path: '/delivery',
            name: 'delivery',
            component: DeliveryView
        },
        {
            path: '/',
            name: 'main',
            component: MainView
        },
        {
            path: '/policy',
            name: 'policy',
            component: PolicyView
        },

        {
            path: '/terms',
            name: 'terms',
            component: TermsView
        },
        {
            path: '/catalog/:id',
            name: 'product',
            component: ProductView
        },
        {
            path: '/reviews',
            name: 'reviews',
            component: ReviewsView
        },
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            beforeEnter: (to, from, next) => {
                to.fullPath = decodeURIComponent(to.fullPath);
                next();
            },
            component: NotFoundView
        },
    ]
})

export default router
