import {
  navigate,
  router
} from './router'


let currentRoute = router.getCurrentRoute(window.location.hash)

if (!currentRoute) {
  navigate('about')
} else {
  navigate(currentRoute.name)
}