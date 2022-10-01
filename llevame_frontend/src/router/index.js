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
    path: "/nuevamascota",
    name: "ApiNuevaMascota",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiNuevaMascota.vue"
      ),
  },
  {
    path: "/adoptar/:new_mascota_id",
    name: "ApiAdoptar",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiAdoptar.vue"
      ),
  },
  {
    path: "/adopciones",
    name: "ApiVerAdopciones",
    //meta: { ifAuth: true },
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiVerAdopciones.vue"
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
    path: "/donar",
    name: "ApiDonar",
    //meta: { ifAuth: true },
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiDonar.vue"
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
  {
    path: "/mascotas",
    name: "ApiVerMascotas",
    //meta: { ifAuth: true },
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiVerMascotas.vue"
      ),
  },
  {
    path: "/editarmascota/:mascota_id",
    name: "ApiEditarMascota",
    props: true,
    component: () =>
      import(
        /* webpackChunkName: "SignUp" */ "../views/ApiEditarMascota.vue"
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