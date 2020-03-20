
import Page from 'app/page'
import * as DataTemplate from 'templates/pages/data.hbs'

export default class DataPage extends Page {

  constructor() {
    super("Podatki")
  }

  template() {
    return DataTemplate({})
  }

}