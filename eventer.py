"""Eventer is a simple event dispaching library.

It provides a simple API to bind and trigger custom named events. Events do not have to be declared before they are bound. ::

    import eventer
    
    def on_edit(page):
        subject = page.path + " is edited"
        sendmail(subject=subject)
    
    eventer.bind("edit", on_edit)
    
    eventer.trigger("edit", page)
    
The API is inspired by event handling in jQuery_ and backbone.js_.

.. _jQuery: http://api.jquery.com/category/events/
.. _backbone.js: http://documentcloud.github.com/backbone/#Events
"""

from collections import defaultdict
import logging

__all__ = ["bind", "unbind", "trigger"]
__version__ = "0.1"
__author__ = "Anand Chitipothu <anand@archive.org>"
__license__ = "GPL v3"

logger = logging.getLogger("eventer")
_callbacks = defaultdict(list)

def bind(event, callback=None):
    """Binds a callback function to an event. 
    
    The callback will be called whenever the specified event is triggered. ::
    
        def on_edit(page):
            subject = page.path + " is edited"
            sendmail(subject=subject)
        
        eventer.bind("edit", on_edit)
    
    This function can also be used as a decorator. ::
    
        @eventer.bind("edit")
        def on_edit(page):
            subject = page.path + " is edited"
            sendmail(subject=subject)
    """
    if callback:
        logger.debug("bind", event, callback)
        _callbacks[event].append(callback)
    else:
        def decorator(callback):
            bind(event, callback)
            return callback
        return decorator
    
def unbind(event, callback):
    """Removes a previously bound callback.
    """
    logger.debug("unbind %s %s", event, callback)
    _callbacks[event].pop(callback, None)
    
def trigger(event, *args, **kwargs):
    """Triggers callbacks for the specified event.
    
    Each callback for the specified event is called with args and kwargs
    passed to this function. Any exception raised by the callback functions is
    ignored.
    """
    logger.debug("trigger %s %s %s", event, args, kwargs)
    # Trigger all callbacks of this event.
    _trigger(event, _callbacks[event], *args, **kwargs)
    
    # Trigger callbacks registered for all events with event as the first argument.
    _trigger(event, _callbacks[None], event, *args, **kwargs)
            
def _trigger(event, callbacks, *args, **kwargs):
    for f in callbacks:
        try:
            f(*args, **kwargs)
        except Exception:
            logger.error("[%s] Failed to trigger a callback (%s)" % (event, f), exc_info=True)