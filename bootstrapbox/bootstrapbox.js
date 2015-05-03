define(['jquery', 'widgets/js/widget_box'], function($, box) {
    var ResponsiveBoxView = box.BoxView.extend({
        render: function() {
            ResponsiveBoxView.__super__.render.apply(this, arguments);
            $(this.el).removeClass('widget-box');
            var that = this;
            [
                'visible_xs_block',
                'visible_xs_inline',
                'visible_xs_inline_block',
                'visible_sm_block',
                'visible_sm_inline',
                'visible_sm_inline_block',
                'visible_md_block',
                'visible_md_inline',
                'visible_md_inline_block',
                'visible_lg_block',
                'visible_lg_inline',
                'visible_lg_inline_block',
                'hidden_xs',
                'hidden_sm',
                'hidden_md',
                'hidden_lg',
                'visible_print_block',
                'visible_print_inline',
                'visible_print_inline_block',
                'hidden_print',
            ].forEach(function(name) {
                var update = function() {
                    var value = that.model.get(name);
                    if (value) {
                        $(that.el).addClass(name.replace(/_/g, '-'))
                    } else {
                        $(that.el).removeClass(name.replace(/_/g, '-'))
                    }
                };
                update();
                that.listenTo(that.model, 'change:' + name, update);
            });
        },
    });

    var BootstrapRowView = ResponsiveBoxView.extend({
        render: function() {
            BootstrapRowView.__super__.render.apply(this, arguments);
            $(this.el).addClass('row');
        }
    });

    var BootstrapContainerView = ResponsiveBoxView.extend({
        _bootstrap_type: 'container',

        render: function() {
            BootstrapContainerView.__super__.render.apply(this, arguments);
            this._set_fluid();
            this.listenTo(this.model, 'change:fluid', this._set_fluid, this);
        },

        _set_fluid: function() {
            if (this.model.get('fluid')) {
                $(this.el)
                    .addClass(this._bootstrap_type + '-fluid')
                    .removeClass(this._bootstrap_type);
            } else {
                $(this.el)
                    .removeClass(this._bootstrap_type + '-fluid')
                    .addClass(this._bootstrap_type);
            }
        },
    });

    var BootstrapColView = ResponsiveBoxView.extend({
        render: function() {
            BootstrapColView.__super__.render.apply(this, arguments);

            var that = this;
            [
                'width',
                'offset',
                'push',
                'pull'
            ].forEach(function(attr) {
                [
                    'xs',
                    'sm',
                    'md',
                    'lg'
                ].forEach(function(size) {
                    var name = [size, attr].join('_');

                    var js_name;
                    if (attr == 'width') {
                        js_name = ['col', size].join('-') + '-';
                    } else {
                        js_name = ['col', size, attr].join('-') + '-';                        
                    }
                    var update = function() {
                        var old_value = that.model.previous(name);
                        var value = that.model.get(name);
                        if (old_value !== null) {
                            $(that.el).removeClass(js_name + String(old_value));
                        }
                        if (value !== null) {
                            $(that.el).addClass(js_name + String(value));
                        }
                    };
                    update();
                    that.listenTo(that.model, 'change:' + name, update);
                });
            });
        },
    });

    return {
        BootstrapContainerView: BootstrapContainerView,
        BootstrapRowView: BootstrapRowView,
        BootstrapColView: BootstrapColView
    }
});