import { serve } from '@hono/node-server'
import { serveStatic } from '@hono/node-server/serve-static'
import { Hono } from 'hono'
import { prettyJSON } from 'hono/pretty-json'
import { obtenerProductos, obtenerProducto, buscarProductos } from './models.js'

const app = new Hono()
app.use(prettyJSON())
// Página principal
app.get('/', serveStatic({ path: './public/index.html' }))
const api = new Hono()
// GET /api/productos → todos los productos

api.get('/productos/:id', (c) => {
  const id = Number(c.req.param('id'))
  const producto = obtenerProducto(id)
  if (!producto) {
    return c.json({ mensaje: 'Producto no encontrado', ok: false }, 404)
  }
  return c.json({ producto })
})

api.get('/buscar', (c) => {
  const texto = c.req.query('texto')
  const productos = buscarProductos(texto || "")
  return c.json({ productos })
})

// TODO: aquí van tus rutas
app.route('/api', api)

app.get('/producto', (c) => {
  const id = c.req.query('id')
  return c.redirect(`/api/productos/${id}`)
})

app.notFound((c) => {
  return c.json({ mensaje: 'No encontrado', ok: false }, 404)
})

serve({ fetch: app.fetch, port: 3000 })
console.log('Servidor en http://localhost:3000')