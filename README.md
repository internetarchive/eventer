# Eventer

Eventer is a simple event dispatching library. It provides a simple API to
bind and trigger custom named events. Events do not have to be declared before
they are bound.

    import eventer
    
    def on_edit(page):
        subject = page.path + " is edited"
        sendmail(subject=subject)
    
    eventer.bind("edit", on_edit)
    
    eventer.trigger("edit", page)
    
The API is inspired by event handling in [jQuery][] and [backbone.js][].

[jQuery]: http://api.jquery.com/category/events/
[backbone.js]: http://documentcloud.github.com/backbone/#Events

## License

Eventer is licensed under GPL v3. See LICENSE file for details.
