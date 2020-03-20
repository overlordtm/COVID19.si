import * as NavbarTop from 'templates/components/navbar-top.hbs'
import {router} from './router'

export default class Page {

  constructor(title, renderTo) {
    this.title = "COVID19 Slovenija"
    if (title != null) {
      this.title = this.title + ": " + title
    }
    this.renderNabvar = true
    renderTo = renderTo || '#content'
    this.renderElm = document.querySelector(renderTo)
  }

  template() {
    return Promise.resolve("<h1>TODO</h1>")
  }
  
  render() {
    // set title
    document.title = this.title

    if (this.renderNabvar === true) {
      let route = router.getCurrentRoute(window.location.hash)

      document.querySelector("#navbar").innerHTML = NavbarTop()

      // add active class to current route in navbar
      Array.from(document.querySelectorAll('#navbar li.nav-item')).forEach((elm) => {
        let link = elm.querySelector("a")
        if (link.href.match(route.matcher) != null) {
          link.classList.add('active')
        }
      })

    }

    let templateP = this.template()
    Promise.resolve(templateP).then(tmpl => {
      // console.log("Rendering page", tmpl, this.name, "to", this.renderElm)
      this.renderElm.innerHTML = tmpl
    })
  }

}