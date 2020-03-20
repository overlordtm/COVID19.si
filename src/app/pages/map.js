
import Page from 'app/page'
import * as MapTemplate from 'templates/pages/map.hbs'

export default class MapPage extends Page {

  constructor() {
    super("Zemljevid")
  }

  template() {
    return MapTemplate({})
  }

}