import { createRouter, createWebHashHistory } from "vue-router";
//import { auth } from "@/LoginService";

const routes = [
  {
    path: "/",
    name: "home",
  },
  {
    path: "/mascotas",
    name: "ApiMascotas",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiMascotas.vue"
      ),
  },
  {
    path: "/adoptar",
    name: "ApiAdoptar",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiAdoptar.vue"
      ),
  },
  {
    path: "/adopciones",
    name: "ApiAdopciones",
    //meta: { ifAuth: true },
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiAdopciones.vue"
      ),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

/*router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.ifAuth)) {
    if (auth.authorized) {
      next();
      return;
    }
    next("/home");
  } else {
    next();
  }
});*/

export default router;