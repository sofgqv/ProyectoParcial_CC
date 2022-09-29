import { createRouter, createWebHashHistory } from "vue-router";
//import { auth } from "@/LoginService";

const routes = [
  {
    path: "/",
    name: "home",
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/HomeView.vue"
      ),
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
  {
    path: "/donaciones",
    name: "ApiDonaciones",
    //meta: { ifAuth: true },
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiDonaciones.vue"
      ),
  },
  {
    path: "/servoluntario",
    name: "ApiSerVoluntario",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiSerVoluntario.vue"
      ),
  },
  {
    path: "/voluntarios",
    name: "ApiVerVoluntarios",
    //meta: { ifAuth: true },
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiVerVoluntarios.vue"
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